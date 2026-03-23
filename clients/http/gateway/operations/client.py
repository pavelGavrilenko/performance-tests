from typing import TypedDict

from httpx import Response, QueryParams

from clients.http.client import HTTPClient


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


class MakeFeeRequestDict(MakeOperationRequestDict):
    pass


class MakeTopUpRequestDict(MakeOperationRequestDict):
    pass


class MakeCashbackRequestDict(MakeOperationRequestDict):
    pass


class MakeTransferRequestDict(MakeOperationRequestDict):
    pass


class MakeBillPaymentRequestDict(MakeOperationRequestDict):
    pass


class MakeCashWithdrawalRequestDict(MakeOperationRequestDict):
    pass


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

    def make_fee_operation_api(self, request: MakeFeeRequestDict) -> Response:
        """
        Выполняет POST-запрос для cоздание операции комиссии.

        :param request: Словарь c телом запроса.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpRequestDict) -> Response:
        """
        Выполняет POST-запрос для cоздание операции пополнения.

        :param request: Словарь c телом запроса.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackRequestDict) -> Response:
        """
        Выполняет POST-запрос для cоздание операции кэшбека.

        :param request: Словарь c телом запроса.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferRequestDict) -> Response:
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

    def make_bill_payment_operation_api(self, request: MakeBillPaymentRequestDict) -> Response:
        """
        Выполняет POST-запрос для cоздание операции оплаты счета.

        :param request: Словарь c телом запроса.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalRequestDict) -> Response:
        """
        Выполняет POST-запрос для cоздание операции снятия наличных.

        :param request: Словарь c телом запроса.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)







