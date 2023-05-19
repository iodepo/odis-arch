# emit a stream
def json2headers:
  def isscalar: type | . != "array" and . != "object";
  def isflat: all(.[]; isscalar);
  paths as $p
  | getpath($p)
  | if type == "array" and isflat then $p
     elif isscalar and (($p[-1]|type) == "string") then $p
     else empty end ;

def json2array($header):
  def value($p):
    try getpath($p) catch null
    | if type == "object" then null else . end;
  [$header[] as $p | value($p)];

def json2csv:
  ( [.[] | json2headers] | unique) as $h
  | ([$h[]|join("_") ],
     (.[]
      | json2array($h)
      | map( if type == "array" then map(tostring)|join("|") else tostring end)))
  | @csv ;