"""Parse all source files and assert removed routing mechanisms stay absent."""
import ast
from common.experiment_config import ROOT


def main():
    count=0
    forbidden=('fall'+'back', 'fell'+'_back', 'bootstrap'+'_m', 'verifier'+'_ext')
    for directory in ('common','cloud','edge','analysis','experiments','tests'):
        for path in (ROOT/directory).rglob('*.py'):
            source=path.read_text(encoding='utf-8-sig')
            tree=ast.parse(source,filename=str(path)); count+=1
            for node in ast.walk(tree):
                names=[]
                if isinstance(node,ast.Name): names=[node.id]
                elif isinstance(node,ast.Attribute): names=[node.attr]
                elif isinstance(node,(ast.FunctionDef,ast.ClassDef)): names=[node.name]
                elif isinstance(node,ast.arg): names=[node.arg]
                elif isinstance(node,ast.Constant) and isinstance(node.value,str) and '\n' not in node.value:
                    names=[node.value]
                if any(term in name.lower() for name in names for term in forbidden):
                    raise AssertionError(f'Removed routing identifier remains: {path}:{node.lineno}')
    source=(ROOT/'edge/edge_client_smart.py').read_text(encoding='utf-8-sig')
    if 'verifier.generate(' in source or "'/generate'" in source:
        raise AssertionError('SD client must only call verify, not target AR')
    print(f'Static AST / removed-route checks passed: {count} Python files')


if __name__=='__main__': main()
