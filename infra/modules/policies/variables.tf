variable "lambda_role_name" {
    description = "Politica de execucao basica de uma lambda"
    type = string
    default = "lambda_basic_execution_policy"
}

variable "policy_lambda_access_resource_s3" {
    description = "Politica de acesso aos buckets do S3"
    type = string
    default = "lambda_access_s3_policy"
}

variable "bucket_s3_etl_arn" {
    description = "Arn do Bucket para Anexar Politica"
    type = string
}

variable "event_bridge_role_name" {
    description = "Nome da politica de execucao do scheduler"
    type = string
    default = "event_bridge_iam"
}

variable "event_bridge_policy_lambda_name" {
    description = "Nome da policy"
    type = string
    default = "event_bridge_policy"
}

variable "aws_lambda_arn" {
    description = "Arn da Lambda para Ativar o Schedule"
    type = string
}
