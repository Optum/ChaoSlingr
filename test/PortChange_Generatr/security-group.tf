resource "aws_security_group" "portchange_generatr_test_notag" {
  name = "portchange_generatr_test_notag"
  tags = "${var.default_tags}"
}

resource "aws_security_group" "portchange_generatr_test_truetag" {
  name = "portchange_generatr_test_truetag"
  tags = "${var.default_tags_true_tag}"
}

resource "aws_security_group" "portchange_generatr_test_falsetag" {
  name = "portchange_generatr_test_falsetag"
  tags = "${var.default_tags_false_tag}"
}
