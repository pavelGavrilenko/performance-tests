from pydantic import BaseModel, HttpUrl


class DocumentSchema(BaseModel):
    """
    Описание структуры документов.
    """
    url: HttpUrl
    document: str


class GetTariffDocumentResponseSchema(BaseModel):
    tariff: DocumentSchema


class GetContractDocumentResponseSchema(BaseModel):
    contract: DocumentSchema
