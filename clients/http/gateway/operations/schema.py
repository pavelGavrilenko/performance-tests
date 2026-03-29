from pydantic import BaseModel, Field, ConfigDict
from strenum import StrEnum

from clients.http.gateway.documents.schema import DocumentSchema
from tools.fakers import fake


class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"


class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class GetOperationsQuerySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    account_id: str = Field(alias="accountId")


class GetOperationsSummaryQuerySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    account_id: str = Field(alias="accountId")


class MakeOperationRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=lambda :fake.amount())
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    category: str = Field(default_factory=lambda :fake.category())


class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    pass


class MakeTopUpOperationRequestSchema(MakeOperationRequestSchema):
    pass


class MakeCashbackOperationRequestSchema(MakeOperationRequestSchema):
    pass


class MakeTransferOperationRequestSchema(MakeOperationRequestSchema):
    pass


class MakeBillPaymentOperationRequestSchema(MakeOperationRequestSchema):
    pass


class MakeCashWithdrawalOperationRequestSchema(MakeOperationRequestSchema):
    pass


class OperationSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")


class OperationReceiptSchema(DocumentSchema):
    pass


class OperationsSummarySchema(BaseModel):
    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")


class GetOperationsResponseSchema(BaseModel):
    operations: list[OperationSchema]


class GetOperationReceiptResponseSchema(BaseModel):
    receipt: OperationReceiptSchema


class GetOperationResponseSchema(BaseModel):
    operation: OperationSchema


class GetOperationSummaryResponseSchema(BaseModel):
    summary: OperationsSummarySchema


class MakePurchaseOperationResponseSchema(BaseModel):
    operation: OperationSchema


class MakeFeeOperationResponseSchema(BaseModel):
    operation: OperationSchema


class MakeTopUpOperationResponseSchema(BaseModel):
    operation: OperationSchema


class MakeCashbackOperationResponseSchema(BaseModel):
    operation: OperationSchema


class MakeTransferOperationResponseSchema(BaseModel):
    operation: OperationSchema


class MakeBillPaymentOperationResponseSchema(BaseModel):
    operation: OperationSchema


class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    operation: OperationSchema

