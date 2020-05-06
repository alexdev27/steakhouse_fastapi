from pydantic import BaseModel, Field
from fastapi import Query


# For easy building openapi arguments for endpoints
class DocInfo:
    def __init__(self, descr='', summ='', res_descr='', status_code=200, resp_model=None):
        self.description = descr
        self.summary = summ
        self.response_description = res_descr
        self.status_code = status_code
        self.response_model = resp_model


class PaginatedResult(BaseModel):
    next: int = Field(..., title='Next page (-1 if there is nowhere to paginate)')
    prev: int = Field(..., title='Previous page (-1 if there is nowhere to paginate)')
    total: int = Field(..., title='Total amount of results')


class Pag(BaseModel):
    # sort:
    limit: int = Query(200, title='Limit!', ge=1, le=200)
    offset: int = Query(1, title='Offset!', ge=1)
    select_fields: str = Query('', title='Comma-separated list of fields to retrieve')

    def dict(self, **kwargs):
        data = super().dict(**kwargs)
        return {'pagination_data': data}


def paginate_model(pagination, mongo_model):
    page = pagination['offset']
    limit = pagination['limit']
    fields = str(pagination['select_fields']).split(',')
    start = (page - 1) * limit
    stop = page * limit

    models = mongo_model.objects()[start:stop]
    total_count_of_models = models.count()

    if fields:
        model_fields = list(mongo_model._fields.keys())
        valid_fields = []
        for field in fields:
            if field in model_fields:
                valid_fields.append(field)
        if valid_fields:
            models = models.only(*valid_fields)

    pagination_result = {
        'next': page + 1 if stop < total_count_of_models else -1,
        'prev': page - 1 if start > 0 and stop < total_count_of_models else -1,
        'total': total_count_of_models,
        'result': list(models)
    }
    return pagination_result
