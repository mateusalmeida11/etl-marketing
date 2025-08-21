output "lambda_execution_role_arn" {
    description = "ARN da role de execucao que sera anexada a Lambda"
    value = aws_iam_role.lambda_exec_role.arn
}

output "aws_scheduler_execution_role_arn" {
    description = "Arn da role de execucao que sera utilizada no Scheduler"
    value = aws_iam_role.event_bridge_role.arl
}
