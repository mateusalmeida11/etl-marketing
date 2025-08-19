output "lambda_execution_role_arn" {
    description = "ARN da role de execucao que sera anexada a Lambda"
    value = aws_iam_role.lambda_exec_role.arn
}
