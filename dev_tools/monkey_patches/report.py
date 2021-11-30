import frappe
from frappe import _
from frappe.utils.safe_exec import get_safe_globals
from frappe.core.doctype.report.report import Report


class CustomReport(Report):
    def execute_script(self, filters):
        frappe.msgprint("Runing in none safe mode", alert=True, indicator="Orange")
        # server script
        loc = {"filters": frappe._dict(filters), "data": None, "result": None}
        safe_exec(self.report_script, None, loc)
        if loc["data"]:
            return loc["data"]
        else:
            return self.get_columns(), loc["result"]


def safe_exec(script, _globals=None, _locals=None, restrict_commit_rollback=False):
    # build globals
    exec_globals = get_safe_globals()
    if _globals:
        exec_globals.update(_globals)

    if restrict_commit_rollback:
        exec_globals.frappe.db.pop("commit", None)
        exec_globals.frappe.db.pop("rollback", None)

    frappe.flags.in_safe_exec = True
    exec(script, exec_globals, _locals)  # pylint: disable=exec-used
    frappe.flags.in_safe_exec = False

    return exec_globals, _locals
