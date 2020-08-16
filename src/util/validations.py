from validate_docbr import CPF


def validate_json(json):
    print(json)
    if json is None:
        raise Exception("Cpf and event are required")

    cpf = json.get('cpf')
    if cpf is None:
        raise Exception("Cpf is required")
    if not validate_cpf(cpf):
        raise Exception("Cpf isn't valid")
    event = json.get('event')
    validate_event(event)


def validate_event(event):
    if event is None:
        raise Exception("Event is required")
    print(event)
    if 'lastSearchBureau' not in event:
        raise Exception("lastSearchBureau is required")

    if 'lastPurchaseCreditCard' in event:
        last_purchase_credit_card = event['lastPurchaseCreditCard']
        if 'date' not in last_purchase_credit_card or 'value' not in last_purchase_credit_card \
                or 'place' not in last_purchase_credit_card or 'cardNumber' not in last_purchase_credit_card:
            raise Exception("The object lastPurchaseCreditCard need this fields: data, value, place, cardNumber")

    if 'financialReports' in event:
        financial_reports = event['financialReports']
        for report in financial_reports:
            if 'bank' not in report or 'type' not in report or 'signal' not in report or 'value' not in report:
                raise Exception("The object in list financialReports need this fields: bank, type, place, value")


def validate_cpf(cpf):
    if cpf:
        cpf_validate = CPF()
        return cpf_validate.validate(doc=cpf)

    return False


def validate_event_put(json):
    event = json.get('event')
    validate_event(event)