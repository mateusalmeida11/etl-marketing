resource "aws_scheduler_schedule" "invoke_lambda" {
  name       = "schedule_etl_marketing"
  group_name = "default"

  flexible_time_window {
    mode = "OFF"
  }

  schedule_expression = "cron(0 9 ? * 2 *)"
  schedule_expression_timezone = America/Sao_Paulo

  target {
    arn      = var.aws_lambda_arn
    role_arn = var.aws_role_arn_scheduler
  }
}
