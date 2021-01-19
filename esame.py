class ExamException(Exception):
  pass

class Diff:
  def __init__(self, ratio=1):
    try:
      assert(ratio != 0)
      assert(isinstance(ratio, (int, float)))
      assert(not isinstance(ratio, bool))

    except:
      raise ExamException("ratio non valido")
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
        assert(len(vals) >= 2)
    except:
        raise ExamException("lista troppo piccola")
    res =[]
    for i in range(len(vals)-1):
      res.append((vals[i+1]- vals[i])/self.ratio)
    return res