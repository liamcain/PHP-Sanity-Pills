import sublime, sublime_plugin

class PhpCreateVarCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		sel = self.view.sel()[0]

		cur_line = self.view.line(sel.begin())

		pt = self.view.find("[a-zA-Z$]", cur_line.begin()).begin()

		if '$' in self.view.substr(pt) or not "constant.other" in self.view.scope_name(sel.begin() - 3):
			self.view.insert(edit, sel.begin(), "=")
			return;

		self.view.insert(edit, pt, "$")
		self.view.insert(edit, sel.begin(), "=")