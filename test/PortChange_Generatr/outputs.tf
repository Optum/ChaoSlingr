output "security_group_id_notag" {
  value = "${aws_security_group.portchange_generatr_test_notag.id}"
}

output "security_group_id_truetag" {
  value = "${aws_security_group.portchange_generatr_test_truetag.id}"
}

output "security_group_id_falsetag" {
  value = "${aws_security_group.portchange_generatr_test_falsetag.id}"
}
