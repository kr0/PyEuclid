from z3 import Solver, Consts, Not, eq, Distinct, simplify
from EuclidZ3.core import *
 

 
def test1():   
    print "=== Loading Core ==="    
    
    solver = Solver()
    solver.push()
    solver.add(language.axioms)
 
    print "=== Starting tests ==="
    
    
    print ">> Let p q r s t u v be distinct points"
    p, q, r, s, t, u, v = Consts('p q r s t u v', language.PointSort)
    solver.add(simplify(Distinct(p,q,r,s,t,u,v), blast_distinct=True))
    
    
    print ">> Let L M N O be distinct lines"
    K, L, M, N, O = Consts('K L M N O', language.LineSort)
    solver.add(simplify(Distinct(K,L,M,N,O), blast_distinct=True))
    
    
    ## Diagram description 
    assumptions = []
     
    assumptions.append(language.OnLine(p,L))
    assumptions.append(language.OnLine(q,L))
    assumptions.append(language.OnLine(p,N))
    assumptions.append(language.OnLine(s,N))
    assumptions.append(language.OnLine(t,N))
    assumptions.append(language.OnLine(p,M))
    assumptions.append(language.OnLine(r,M))
    assumptions.append(language.OnLine(q,O))
    assumptions.append(language.OnLine(s,O))
    assumptions.append(language.OnLine(r,O))
    assumptions.append(language.OnLine(q,K))
    assumptions.append(language.OnLine(t,K))
    assumptions.append(Not(language.OnLine(r,L)))
    assumptions.append(language.Between(p,s,t))
    assumptions.append(language.Between(q,s,r))
    assumptions.append(language.Between(s,u,t))
    assumptions.append(Not(p == q))
    assumptions.append(language.Between(p,q,v))
  
    
    
    print ">> Assume " + str(assumptions)
    solver.add(assumptions)
    print "      << z3: " + str(solver.check())
     
     
    ## Satisfied 
    solver.push()
    solver.add(True)
    print ">> Hence True"    
    print "      << z3: " + str(solver.check())
    solver.pop()
    
    ## Satisfied  
    solver.push()
    solver.add(Not(language.SameSide(s,t,O)))
    print ">> Hence s and t are on opposite sides of O"
    print "      << z3: " + str(solver.check())
    solver.pop()
    
    ## Satisfied  
    solver.push()
    solver.add(language.SameSide(u,t,M))
    print ">> Hence u and t are on same side of M"
    print "      << z3: " + str(solver.check())
    solver.pop()
    
    ## unsatisfied  
    solver.push()
    solver.add(language.SameSide(p,t,O))
    print ">> Hence p and t are on same side of O"
    print "      << z3: " + str(solver.check())
    solver.pop()
    
    ## unsatisfied  
    solver.push()
    solver.add(language.SameSide(s,t,O))
    print ">> Hence s and t are on same side of O"
    print "      << z3: " + str(solver.check())
    solver.pop()
    
    ## unsatisfied  
    solver.push()
    solver.add(Not(language.SameSide(s,t,M)))
    print ">> Hence s and t are on opposite sides of M"
    print "      << z3: " + str(solver.check())
    solver.pop()
    
    ## unsatisfied  
    solver.push()
    solver.add(Not(language.SameSide(u,t,M)))
    print ">> Hence u and t are on opposite sides of M"
    print "      << z3: " + str(solver.check())
    solver.pop()
    
    ## unsatisfied  
    solver.push()
    solver.add(language.Between(s,p,t))
    print ">> Hence p is between s and t"
    print "      << z3: " + str(solver.check())
    solver.pop()
    
    ## unsatisfied  
    solver.push()
    solver.add(M == N)
    print ">> Hence p is between s and t"
    print "      << z3: " + str(solver.check())
    solver.pop()
    
    ## unsatisfied  
    solver.push()
    solver.add(language.Between(q,s,u))
    print ">> Hence s is between q and u"
    print "      << z3: " + str(solver.check())
    solver.pop()
    
    ## unsatisfied  
    solver.push()
    solver.add(Not( language.Segment(s,u) < language.Segment(s,t)))
    print ">> Hence seg su is less than seg st"
    print "      << z3: " + str(solver.check())
    solver.pop()
    
    ## unsatisfied  
    solver.push()
    solver.add(L==K)
    print ">> Hence L = K"
    print "      << z3: " + str(solver.check())
    solver.pop()

 
 
 
def testPointConstructions():
    """
    This test serves as an example of various constructions.
    In the absence of a way of checking equality of z3 objects,
    this test prints the prereqs and conclusions of constructions rules.
    We can then check these by eye for correct pre and post requirements.
    
    This is independent of the proof checker checking/asserting
    those requirements to Z3.
    
    Each corresponds to pages 715-717 of "A Formal System For Euclid's Elements"
    by Avigad et al.
    """
    
    print "\n=== testPointConstruction ==="
    print "> let p be a distinct point"
    p = Point("p")
    print str(p)  
    
    print "> let p be a non-distinct point"
    p = Point("p",False)
    print str(p)  
    
    print "> let p be a point on L"
    L = Line('L')
    p = Point('p')
    p.onLine(L)
    print str(p)
    
    print "> let p be a point on L between b and c"
    L = Line('L')
    p = Point('p')
    p.onLine(L)
    b = Point('b')
    b.onLine(L)
    c = Point('c')
    c.onLine(L)
    p.between(b,c)
    print str(b)
    print str(c)
    print str(p)
    
    
    print '> let p be a point on L extending the segment from b to c'
    ## TODO: for avigad: this example shows that although the point p
    ## doesn't have all of the conclusions and prerequisites listed
    ## when the points b, c, and the line L are passed to the proof checker,
    ## collectively their prereqs and conclusions are exactly those listed
    ## by the construction rule 4, pg 716.
    b = Point('b')
    c = Point('c')
    L = Line('L')
    b.onLine(L)
    c.onLine(L)
    p = Point('p')
    p.onLine(L)
    c.between(b, p)
    print str(p)
    print str(c)
    print str(b)
    
    print '> let p be a point on the same side of L as b'
    p = Point('p')
    b = Point('b')
    L = Line('L')
    p.sameside(b, L)
    print str(p)
    
    print '> let p be a point on the side L opposite b'
    b = Point('b')
    L = Line('L')
    p = Point('p')
    p.opposite(b, L)
    print str(p)
    
    print '> let p be a point on circle alpha'
    p = Point("p")
    alpha = Circle("alpha")
    p.onCircle(alpha)
    print str(p)
    print str(alpha)
    
    
    print '> let p be a point inside circle alpha'
    alpha = Circle("alpha")
    p = Point("p")
    p.inside(alpha)
    print str(p)
    print str(alpha)
    
    print '> let p be a point outside circle alpha'
    alpha = Circle("alpha")
    p = Point("p")
    p.outside(alpha)
    print str(p)
    
    
def testLinesAndCircles():
    """
    This test checks that construction rules for lines and circles
    list correct pre and post requirements. This test is also an example
    of how to use this framework.

    
    Each corresponds to pages 715-717 of "A Formal System For Euclid's Elements"
    by Avigad et al.
    """
    
    print "\n=== testLinesAndCirclesConstruction ==="    
    print "> let L be the line through a and b"
    L = Line("L")
    a = Point("a")
    b = Point("b")
    L.through(a,b)
    print str(L)
    
    print "> let alpha be the circle with center a passing through b"
    a = Point("a")
    b = Point("b")
    alpha = Circle("alpha")
    alpha.centerThrough(a, b)
    print str(alpha)
    
    

    
       
if __name__ == '__main__':
    print "\n=== Running Tests for EuclidZ3 ==="
#     test1()
    testPointConstructions()
    testLinesAndCircles()
    
    
    
    
    
    
    
    