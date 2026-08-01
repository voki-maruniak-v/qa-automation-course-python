test_report =" Login test | FAILED | Invalid password message "

clean_report = test_report.strip()

print(test_report)
print(clean_report)

updated_report = clean_report.replace('FAILED', 'PASSED')
print(updated_report)

report_parts = updated_report.split(' | ')
print(report_parts)
print(type(report_parts))

test_steps = ["Open application", "Enter login", "Check result"]
print(" -> ".join(test_steps))
