class Case:
    def __init__(self, case_id, description, owner, status, date, time, customer_id, category, priority, resolved_at=None, notes=None):
        self.case_id = case_id
        self.description = description
        self.owner = owner
        self.status = status
        self.date = date
        self.time = time
        self.customer_id = customer_id
        self.category = category
        self.priority = priority
        self.resolved_at = resolved_at
        self.notes = notes if notes is not None else []