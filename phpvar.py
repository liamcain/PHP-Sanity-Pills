import sublime, sublime_plugin

class PhpFunctionsAutoComplete(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        
        completions = []

    	if not view.match_selector(locations[0],
                "text.html, source.php"):
            return []

        reg_completions = view.find_all("\\$[a-z_A-Z0-9]+")

        for c in reg_completions:
            completions.append(view.substr(c).replace("$", "\$"))

        for x in view.find_all("(?<![$])\b[a-zA-Z]+"):
            completions.append(view.substr(x))

        return [(x.replace('\\$', ''), x) for x in sorted(list(set(completions)))]