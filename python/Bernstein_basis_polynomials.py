
def monomial_to_bernstein_degree2(monomial_coefficients):
    (a0, a1, a2) = monomial_coefficients
    return (a0, a0 + ((1/2) * a1), a0 + a1 + a2)

def evaluate_bernstein_degree2(bernstein_coefficients, t):
    (b0, b1, b2) = bernstein_coefficients
    
    s = 1 - t
    b01 = (s * b0) + (t * b1)
    b12 = (s * b1) + (t * b2)
    b012 = (s * b01) + (t * b12)
    return b012

def monomial_to_bernstein_degree3(monomial_coefficients):
    (a0, a1, a2, a3) = monomial_coefficients
    return (a0, a0 + ((1/3) * a1),
            a0 + ((2/3) * a1) + ((1/3) * a2),
            a0 + a1 + a2 + a3)

def evaluate_bernstein_degree3(bernstein_coefficients, t):
    (b0, b1, b2, b3) = bernstein_coefficients
    
    s = 1 - t
    b01 = (s * b0) + (t * b1)
    b12 = (s * b1) + (t * b2)
    b23 = (s * b2) + (t * b3)
    b012 = (s * b01) + (t * b12)
    b123 = (s * b12) + (t * b23)
    b0123 = (s * b012) + (t * b123)
    return b0123

def bernstein_degree2_to_degree3(bernstein_coefficients):
    (b0, b1, b2) = bernstein_coefficients
    return (b0, ((1/3) * b0) + ((2/3) * b1),
            ((2/3) * b1) + ((1/3) * b2), b2)

def evaluate_monomial_degree2(monomial_coefficients, t):
    (a0, a1, a2) = monomial_coefficients

    return a0 + (t * (a1 + (t * a2)))

def evaluate_monomial_degree3(monomial_coefficients, t):
    (a0, a1, a2, a3) = monomial_coefficients
    
    return a0 + (t * (a1 + (t * (a2 + (t * a3)))))

pmono2 = (1, 0, 0)
qmono2 = (1, 2, 3)
pbern2 = monomial_to_bernstein_degree2(pmono2)
qbern2 = monomial_to_bernstein_degree2(qmono2)
print("Subprogram (1) examples:")
print("  mono", pmono2, " --> bern", pbern2)
print("  mono", qmono2, " --> bern", qbern2)


print("Subprogram (2) examples:")
for x in (0.25, 7.50):
    print("  p(", x, ") = ", evaluate_bernstein_degree2(pbern2, x),
          " ( mono: ", evaluate_monomial_degree2(pmono2, x), ")")
for x in (0.25, 7.50):
    print("  q(", x, ") = ", evaluate_bernstein_degree2(qbern2, x),
          " ( mono: ", evaluate_monomial_degree2(qmono2, x), ")")


pmono3 = (1, 0, 0, 0)
qmono3 = (1, 2, 3, 0)
rmono3 = (1, 2, 3, 4)
pbern3 = monomial_to_bernstein_degree3(pmono3)
qbern3 = monomial_to_bernstein_degree3(qmono3)
rbern3 = monomial_to_bernstein_degree3(rmono3)
print("Subprogram (3) examples:")
print("  mono", pmono3, " --> bern", pbern3)
print("  mono", qmono3, " --> bern", qbern3)
print("  mono", rmono3, " --> bern", rbern3)


print("Subprogram (4) examples:")
for x in (0.25, 7.50):
    print("  p(", x, ") = ", evaluate_bernstein_degree3(pbern3, x),
          " ( mono: ", evaluate_monomial_degree3(pmono3, x), ")")
for x in (0.25, 7.50):
    print("  q(", x, ") = ", evaluate_bernstein_degree3(qbern3, x),
          " ( mono: ", evaluate_monomial_degree3(qmono3, x), ")")
for x in (0.25, 7.50):
    print("  r(", x, ") = ", evaluate_bernstein_degree3(rbern3, x),
          " ( mono: ", evaluate_monomial_degree3(rmono3, x), ")")


print("Subprogram (5) examples:")
pbern3a = bernstein_degree2_to_degree3(pbern2)
qbern3a = bernstein_degree2_to_degree3(qbern2)
print("  bern", pbern2, " --> bern", pbern3a)
print("  bern", qbern2, " --> bern", qbern3a)
