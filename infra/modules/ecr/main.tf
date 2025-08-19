resource "aws_ecr_repository" "ecr_etl_marketing" {
  name = var.ecr_hub_etl_marketing
  image_tag_mutability = "MUTABLE"
  image_scanning_configuration {
    scan_on_push = true
  }
}
