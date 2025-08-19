output "ecr_repositor_url" {
    description = "URL de saída do repositório do ECR"
    value = aws_ecr_repository.ecr_etl_marketing.repository_url
}
