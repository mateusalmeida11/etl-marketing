variable "url_repos_etl_marketing" {
    description = "URL do repositorio no ECR onde ficara a imagem Docker"
    type = string
}

variable "arn_policy_lambda_execution" {
    description = "ARN da Role que será anexada a Lambda"
    type = string
}

variable "aws_lambda_name_layer" {
    description = "Nome da AWS Lambda que fara o ETL"
    type = string
    default = "lambda-etl-marketing-bronze"
}

variable "image_tag" {
    description = "Tag da Imagem que Será Passada Nativamente Pelo Github"
    type = string
}
