import time
from time import sleep

import grpc

from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserRequest, CreateUserResponse
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub
from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import AccountsGatewayServiceStub
from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import OperationsGatewayServiceStub
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import \
    OpenDebitCardAccountRequest, OpenDebitCardAccountResponse
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import (
    MakeTopUpOperationRequest,
    MakeTopUpOperationResponse
)
from contracts.services.gateway.operations.rpc_get_operation_receipt_pb2 import (
    GetOperationReceiptRequest,
    GetOperationReceiptResponse
)
from contracts.services.operations.operation_pb2 import OperationStatus

# Используем генератор фейковых данных, созданный ранее
from tools.fakers import fake

# Устанавливаем соединение с gRPC-сервером по адресу localhost:9003
channel = grpc.insecure_channel("localhost:9003")

# Создаём gRPC-клиент для UsersGatewayService
users_gateway_service = UsersGatewayServiceStub(channel)
# Создаём gRPC-клиент для AccountsGatewayService
accounts_gateway_service = AccountsGatewayServiceStub(channel)
# Создаём gRPC-клиент для OperationsGatewayService
operations_gateway_service = OperationsGatewayServiceStub(channel)


# Формируем запрос на создание пользователя с рандомными данными
create_user_request = CreateUserRequest(
    email=fake.email(),
    last_name=fake.last_name(),
    first_name=fake.first_name(),
    middle_name=fake.middle_name(),
    phone_number=fake.phone_number()
)

# Отправляем запрос и получаем ответ
create_user_response: CreateUserResponse = users_gateway_service.CreateUser(create_user_request)
print('Create user response:', create_user_response)

# Формируем запрос на создание карты для созданого пользователя
open_debit_request = OpenDebitCardAccountRequest(
    user_id=create_user_response.user.id
)

# Отправляем запрос и получаем ответ
open_debit_response: OpenDebitCardAccountResponse = accounts_gateway_service.OpenDebitCardAccount(
    open_debit_request
)
print('Open debit card account response:', open_debit_response)

# Формируем запрос на операцию пополнения
make_topup_operation_request = MakeTopUpOperationRequest(
    status=OperationStatus.OPERATION_STATUS_COMPLETED,  # Статус операции (выполнена)
    amount=fake.amount(),  # Сумма покупки
    card_id=open_debit_response.account.cards[0].id,  # ID первой карты счёта
    account_id=open_debit_response.account.id  # ID счёта
)


# Отправляем запрос и получаем ответ
make_topup_operation_response: MakeTopUpOperationResponse = operations_gateway_service.MakeTopUpOperation(
    make_topup_operation_request
)
print('Make operation topup response:', make_topup_operation_response)

# Формируем запрос на чек
get_operations_request = GetOperationReceiptRequest(
    operation_id=make_topup_operation_response.operation.id
)

# Отправляем запрос и получаем ответ
get_operations_response: GetOperationReceiptRequest = operations_gateway_service.GetOperationReceipt(
    get_operations_request
)
print('Get operation receipt response:', get_operations_response)
