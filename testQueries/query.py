from rdflib import Graph
from owlrl import DeductiveClosure, OWLRL_Semantics

# 1. Load graphs
g = Graph()
# g.parse("ontology.ttl", format="turtle")
g.parse("../data/wiki_db_cleaned_2.ttl", format="turtle")

# print(f"Triples before reasoning: {len(g)}")

# 2. Run OWL RL reasoning
# DeductiveClosure(OWLRL_Semantics).expand(g)

# print(f"Triples after reasoning: {len(g)}")

# 3. Example checks
q1 = """
PREFIX ex: <http://example.org/movie/>

SELECT (COUNT(?m) AS ?movieCount)
WHERE {
  ?m a ex:Movie .
}
"""

q2 = """
PREFIX ex: <http://example.org/movie/>

SELECT (COUNT(?a) AS ?movieCount)
WHERE {
  {
    SELECT ?a
    WHERE {
      ?a ex:genre ?g .
    }
    GROUP BY ?a
    HAVING (COUNT(DISTINCT ?g) = 3)
  }
}

"""

print("Actors:", list(g.query(q2))[0][0])