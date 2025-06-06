# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CeMrkJ2pz12Il9Qyf-AvD4Ik85TsL8CQ
"""

!pip install experta

!pip install --upgrade frozendict

nfrom experta import *

class Diagnosis(KnowledgeEngine):

    @Rule(Fact(cough=True) & Fact(fever=True) & Fact(fatigue=True))
    def flu(self):
        print("Diagnosis: You may have the Flu.")

    @Rule(Fact(cough=True) & Fact(fever=True) & Fact(breathing_difficulty=True))
    def pneumonia(self):
        print("Diagnosis: You may have Pneumonia.")

    @Rule(Fact(sneezing=True) & Fact(runny_nose=True) & Fact(cough=False))
    def cold(self):
        print("Diagnosis: You may have a Common Cold.")

    @Rule(Fact(sore_throat=True) & Fact(fever=True))
    def throat_infection(self):
        print("Diagnosis: You may have a Throat Infection.")

    @Rule(Fact(cough=False) & Fact(fever=False) & Fact(fatigue=False))
    def healthy(self):
        print("Diagnosis: You seem to be healthy.")

def get_input():
    """Helper function to get user input as boolean (yes/no)."""
    def ask_question(question):
        return input(question + " (yes/no): ").strip().lower() == "yes"

    return {
        "cough": ask_question("Do you have a cough?"),
        "fever": ask_question("Do you have a fever?"),
        "fatigue": ask_question("Do you feel fatigued?"),
        "breathing_difficulty": ask_question("Do you have breathing difficulties?"),
        "sneezing": ask_question("Are you sneezing?"),
        "runny_nose": ask_question("Do you have a runny nose?"),
        "sore_throat": ask_question("Do you have a sore throat?")
    }

# Running the Expert System
if __name__ == "__main__":
    symptoms = get_input()
    engine = Diagnosis()
    engine.reset()  # Reset the knowledge engine

    for symptom, present in symptoms.items():
        engine.declare(Fact(**{symptom: present}))  # Declare facts

    engine.run()  # Run the inference engine

from experta import *

class SistemPakarMedis(KnowledgeEngine):

    @Rule(Fact(demam=True) & Fact(batuk=True))
    def flu(self):
        print("Diagnosis: Flu.")

    @Rule(Fact(sakit_tenggorokan=True) & Fact(demam=True))
    def throat_infection(self):
        print("Diagnosis: Radang Tenggorokan.")

    @Rule(Fact(batunyeri_otot=True) & Fact(nyeri_perut=True))
    def pneumonia(self):
        print("Diagnosis: Pneumonia.")

# Running the Expert System
engine = SistemPakarMedis()
engine.reset()
engine.declare(Fact(demam=True))
engine.declare(Fact(sakit_tenggorokan=True))  # Input symptoms
engine.run()

def forward_chaining(facts, rules):
    inferred = set(facts)
    changed = True

    while changed:
        changed = False
        for rule in rules:
            if set(rule["if"]).issubset(inferred) and rule["then"] not in inferred:
                inferred.add(rule["then"])
                changed = True
    return inferred

facts = {"has_feathers", "can_fly", "lays_eggs"}
rules = [
    {"if": ["has_feathers", "can_fly"], "then": "is_bird"},
    {"if": ["lays_eggs", "is_bird"], "then": "is_chicken"}
]

result = forward_chaining(facts, rules)
print("Inferred facts:", result)

from experta import *

class CareerExpert(KnowledgeEngine):

    @Rule(Fact(career="Software Engineer"),
          Fact(logic=True), Fact(math=True), Fact(coding=True))
    def software_engineer(self):
        print("You qualify to be a Software Engineer!")

    @Rule(Fact(career="Doctor"),
          Fact(medical=True), Fact(science=True), Fact(problem_solving=True))
    def doctor(self):
        print("You qualify to be a Doctor!")

# Running the Expert System
engine = CareerExpert()
engine.reset()

# Set a goal: Check if the user can be a Software Engineer
engine.declare(Fact(career="Doctor"))
engine.declare(Fact(medical=True))
engine.declare(Fact(science=True))
engine.declare(Fact(problem_solving=True))  # Skills possessed

engine.run()

def backward_chaining(goal, facts, rules):
    if goal in facts:
        return True
    for rule in rules:
        if rule["then"] == goal:
            if all(backward_chaining(cond, facts, rules) for cond in rule["if"]):
                return True
    return False

facts = ("likes_computers", "solves_problems")

rules = [
    {"if": ("likes_computers", "solves_problems"), "then": "should_be_engineer"},
    {"if": ("should_be_engineer", "likes_programming"), "then": "software_engineer"}
]

goal = "software_engineer"
result = backward_chaining(goal, facts, rules)
print(f"Is '{goal}' provable? ->", result)

def forward_chaining(facts, rules):
    inferred = set(facts)
    changed = True

    while changed:
        changed = False
        for rule in rules:
            if rule["if"].issubset(inferred) and rule["then"] not in inferred:
                inferred.add(rule["then"])
                changed = True
    return inferred

# 🔸 Variabel facts dan rules
facts = {"has_wheels", "has_engine", "has_four_wheels"}

rules = [
    {"if": {"has_wheels", "has_engine"}, "then": "is_vehicle"},
    {"if": {"is_vehicle", "has_two_wheels"}, "then": "is_motorcycle"},
    {"if": {"is_vehicle", "has_four_wheels"}, "then": "is_car"}
]

# 🔍 Jalankan fungsi dan print hasil inferensi
result = forward_chaining(facts, rules)
print("Hasil inferensi:", result)

def backward_chaining(goal, facts, rules):
    if goal in facts:
        return True
    for rule in rules:
        if rule["then"] == goal:
            if all(backward_chaining(cond, facts, rules) for cond in rule["if"]):
                return True
    return False

# 🔸 1. Facts (initial known information)
facts = {"has_feathers", "has_small_wings"}

# 🔸 2. Rules (inference rules)
rules = [
    {"if": {"is_bird", "cannot_fly"}, "then": "is_penguin"},
    {"if": {"has_feathers"}, "then": "is_bird"},
    {"if": {"has_small_wings"}, "then": "cannot_fly"}
]

# 🔸 3. Goal (what we want to prove)
goal = "is_penguin"

# 🔍 Run backward chaining inference
result = backward_chaining(goal, facts, rules)
print(f"Is '{goal}' provable? ->", result)