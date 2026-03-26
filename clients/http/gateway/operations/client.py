from typing import TypedDict

from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class GetOperationsQueryDict(TypedDict):
    accountId: str


class GetOperationsSummaryQueryDict(TypedDict):
    accountId: str


class MakeOperationRequestDict(TypedDict):
    status: str
    amount: float
    cardId: str
    accountId: str


class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    category: str


class MakeFeeOperationRequestDict(MakeOperationRequestDict):
    pass


class MakeTopUpOperationRequestDict(MakeOperationRequestDict):
    pass


class MakeCashbackOperationRequestDict(MakeOperationRequestDict):
    pass


class MakeTransferOperationRequestDict(MakeOperationRequestDict):
    pass


class MakeBillPaymentOperationRequestDict(MakeOperationRequestDict):
    pass


class MakeCashWithdrawalOperationRequestDict(MakeOperationRequestDict):
    pass


class OperationDict(TypedDict):
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str


class OperationReceiptDict(TypedDict):
    url: str
    document: str


class OperationsSummaryDict(TypedDict):
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float


class GetOperationsResponseDict(TypedDict):
    operations: list[OperationDict]


class GetOperationReceiptResponseDict(TypedDict):
    receipt: OperationReceiptDict


class GetOperationResponseDict(TypedDict):
    operation: OperationDict


class GetOperationSummaryResponseDict(TypedDict):
    summary: OperationsSummaryDict


class MakePurchaseOperationResponseDict(MakeOperationRequestDict):
    operation: OperationDict


class MakeFeeOperationResponseDict(MakeOperationRequestDict):
    operation: OperationDict


class MakeTopUpOperationResponseDict(MakeOperationRequestDict):
    operation: OperationDict


class MakeCashbackOperationResponseDict(MakeOperationRequestDict):
    operation: OperationDict


class MakeTransferOperationResponseDict(MakeOperationRequestDict):
    operation: OperationDict


class MakeBillPaymentOperationResponseDict(MakeOperationRequestDict):
    operation: OperationDict


class MakeCashWithdrawalOperationResponseDict(MakeOperationRequestDict):
    operation: OperationDict


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение списка операций пользователя.

        :param query: Словарь с параметрами запроса, например: {'userId': '123'}.
        :return: Объект httpx.Response с данными об операциях.
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получение чека по операции по operation_id

        :param operation_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получение информации об операции по operation_id

        :param operation_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение статистики по операциям для определенного счета.

        :param query: Словарь с параметрами запроса, например: {'userId': '123'}.
        :return: Объект httpx.Response с данными об операциях.
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для cоздание операции комиссии.

        :param request: Словарь c телом запроса.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для cоздание операции пополнения.

        :param request: Словарь c телом запроса.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для cоздание операции кэшбека.

        :param request: Словарь c телом запроса.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для cоздание операции перевода.

        :param request: Словарь c телом запроса.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для cоздание операции покупки.

        :param request: Словарь c телом запроса.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для cоздание операции оплаты счета.

        :param request: Словарь c телом запроса.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для cоздание операции снятия наличных.

        :param request: Словарь c телом запроса.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        response = self.get_operation_receipt_api(operation_id=operation_id)
        return response.json()

    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        response = self.get_operation_api(operation_id=operation_id)
        return response.json()

    def get_operations_summary(self, account_id: str) -> GetOperationSummaryResponseDict:
        query = GetOperationsSummaryQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query)
        return response.json()

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseDict:
        request = MakeFeeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseDict:
        request = MakeTopUpOperationRequestDict(
            status="COMPLETED",
            amount=66.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseDict:
        request = MakeCashbackOperationRequestDict(
            status="COMPLETED",
            amount=77.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseDict:
        request = MakeTransferOperationRequestDict(
            status="COMPLETED",
            amount=88.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseDict:
        request = MakePurchaseOperationRequestDict(
            status="COMPLETED",
            amount=99.77,
            cardId=card_id,
            accountId=account_id,
            category="car_wash"
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseDict:
        request = MakeBillPaymentOperationRequestDict(
            status="COMPLETED",
            amount=111.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseDict:
        request = MakeCashWithdrawalOperationRequestDict(
            status="COMPLETED",
            amount=122.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр AccountsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AccountsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())







