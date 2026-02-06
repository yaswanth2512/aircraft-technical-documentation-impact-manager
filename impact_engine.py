class ImpactAssessmentEngine:

    def assess_impact(self, change, manuals):
        impacted = []

        for manual in manuals:
            if manual.ata_chapter == change["ata"]:
                impacted.append(manual)

        return impacted

    def determine_actions(self):
        return [
            "Technical Review Required",
            "Documentation Update Required",
            "Compliance Validation Required"
        ]
