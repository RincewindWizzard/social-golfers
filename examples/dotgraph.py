#!/usr/bin/python3
import graphviz as gv
from subprocess import call

colors = ['#8b8378', '#76eec6', '#66cdaa', '#838b8b', '#cdb79e', '#8b7d6b', '#8a2be2', '#ff4040', '#deb887', '#cdaa7d', '#5f9ea0', '#7ac5cd', '#7fff00', '#7fff00', '#ff7f24', '#ee7621', '#ff7f50', '#ff7256', '#ee6a50', '#6495ed', '#8b8878', '#00ffff', '#00ffff', '#00eeee', '#00cdcd', '#ffb90f', '#eead0e', '#cd950c', '#bdb76b', '#bcee68', '#a2cd5a', '#ff8c00', '#ff7f00', '#9932cc', '#bf3eff', '#b23aee', '#9a32cd', '#e9967a', '#8fbc8f', '#9bcd9b', '#79cdcd', '#00ced1', '#ff1493', '#ff1493', '#ee1289', '#00bfff', '#00bfff', '#00b2ee', '#1e90ff', '#1e90ff', '#1c86ee', '#ffd700', '#ffd700', '#eec900', '#cdad00', '#daa520', '#ffc125', '#eeb422', '#cd9b1d', '#7a7a7a', '#7d7d7d', '#7f7f7f', '#828282', '#858585', '#878787', '#8a8a8a', '#8c8c8c', '#8f8f8f', '#919191', '#949494', '#969696', '#999999', '#9c9c9c', '#9e9e9e', '#a1a1a1', '#a3a3a3', '#a6a6a6', '#a8a8a8', '#ababab', '#adadad', '#b0b0b0', '#b3b3b3', '#b5b5b5', '#b8b8b8', '#bababa', '#adff2f', '#7a7a7a', '#7d7d7d', '#7f7f7f', '#828282', '#858585', '#878787', '#8a8a8a', '#8c8c8c', '#8f8f8f', '#919191', '#949494', '#969696', '#999999', '#9c9c9c', '#9e9e9e', '#a1a1a1', '#a3a3a3', '#a6a6a6', '#a8a8a8', '#ababab', '#adadad', '#b0b0b0', '#b3b3b3', '#b5b5b5', '#b8b8b8', '#bababa', '#838b83', '#ff69b4', '#ff6eb4', '#ee6aa7', '#cd6090', '#cd5c5c', '#ff6a6a', '#ee6363', '#cd5555', '#8b8b83', '#cdc673', '#8b8386', '#7cfc00', '#8b8970', '#9ac0cd', '#68838b', '#f08080', '#7a8b8b', '#cdbe70', '#cd8c95', '#ffa07a', '#ffa07a', '#ee9572', '#cd8162', '#20b2aa', '#8db6cd', '#8470ff', '#778899', '#778899', '#a2b5cd', '#6e7b8b', '#8b8b7a', '#ff00ff', '#ff00ff', '#ee00ee', '#cd00cd', '#ff34b3', '#ee30a7', '#cd2990', '#66cdaa', '#ba55d3', '#d15fee', '#b452cd', '#9370db', '#ab82ff', '#9f79ee', '#8968cd', '#7b68ee', '#00fa9a', '#48d1cc', '#8b7d7b', '#cdb38b', '#c0ff3e', '#b3ee3a', '#9acd32', '#ffa500', '#ffa500', '#ee9a00', '#da70d6', '#cd69c9', '#98fb98', '#9aff9a', '#90ee90', '#7ccd7c', '#96cdcd', '#668b8b', '#db7093', '#ff82ab', '#ee799f', '#cd6889', '#cdaf95', '#cd853f', '#cd919e', '#cd96cd', '#8b668b', '#a020f0', '#9b30ff', '#912cee', '#7d26cd', '#bc8f8f', '#cd9b9b', '#4169e1', '#4876ff', '#436eee', '#fa8072', '#ff8c69', '#ee8262', '#cd7054', '#f4a460', '#54ff9f', '#4eee94', '#43cd80', '#8b8682', '#ff8247', '#ee7942', '#cd6839', '#7ec0ee', '#6ca6cd', '#6a5acd', '#836fff', '#7a67ee', '#6959cd', '#708090', '#9fb6cd', '#6c7b8b', '#708090', '#8b8989', '#00ff7f', '#00ff7f', '#4682b4', '#63b8ff', '#5cacee', '#4f94cd', '#d2b48c', '#ffa54f', '#ee9a49', '#cd853f', '#8b7b8b', '#ff6347', '#ff6347', '#ee5c42', '#40e0d0', '#00f5ff', '#00e5ee', '#00c5cd', '#d02090', '#ff3e96', '#ee3a8c', '#cd3278', '#cdba96', '#8b7e66', '#ffff00', '#ffff00', '#eeee00', '#cdcd00', '#9acd32']

def graph(solution):
  c = 0
  g = gv.Graph(format='svg')
  for week in solution:
    for group in week:
      gcolor = colors[c % len(colors)]
      c += 1
      for i, p1 in enumerate(group):
        for j in range(i + 1, len(group)):
          g.edge(str(p1), str(group[j]), color=gcolor, penwidth='2')
  return g

def showGraph(solution, layout='twopi'):
  gv = graph(solution)
  gv.render(filename='/tmp/graph.gv')
  call([layout, '-Tsvg', '/tmp/graph.gv', '-o', '/tmp/graph.svg'])
  call(['eog', '/tmp/graph.svg'])


