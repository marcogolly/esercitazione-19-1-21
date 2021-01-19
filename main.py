class ExamException(Exception):
  pass

class Diff:
  def __init__(self, ratio=1):
    try:
            
      assert(ratio >=1)
      assert(isinstance(ratio, int))
      assert(not isinstance(ratio, bool))

    except:
      raise ExamException("non valido")
    self.ratio = ratio

  def compute(self, vals):
    #tests
    try:
        #testo che vals sia una lista
        assert(isinstance(vals, list))
        #testo che ogni val in vals sia int o float
        for val in vals:
            assert(not isinstance(val, (bool)))            
            assert(isinstance(val, (int, float)))
    except:
        raise ExamException("formato lista non corretto")
    try:
        #testo che la lista non sia vuota o più piccola della len di finestra
        assert(len(vals) >= 2)
    except:
        raise ExamException("lista troppo piccola")
    res =[]
    for i in range(len(vals)-1):
      res.append((vals[i+1]- vals[i])/self.ratio)
    return res

diff = Diff()

result = diff.compute([2,4,8,16])

print(result)
test = [[2,4,8,16],[], [1,2,3],[1.2, 2.3, 4.5, 6.3, 4.6],"ciao",10,[1,2,3,[4,5]],["1","2", "3", "4"], [1,2, True],12.1,[None],None,[-12,-23,-5, 5, 1.4],[-12,-23,-5, 5, 1.4, "ciao"],[None, 1,2,3]]
for t in test:
  try:
    print("provo {}:".format(t), diff.compute(t))
  except ExamException as e:
    print("provo {}:".format(t),e)
