variable "ecr_hub_etl_marketing" {
    description = "Repositório no ECR que armazenará a imagem para AWS Lambda do ETL de Marketing"
    type = string
    default = "etl_marketing_lambda"
}
