def auto_remediate(event):
    if event['type'] == 'non_compliance':
        print('Remediation triggered.')