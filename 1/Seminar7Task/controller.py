import model
import view
import test_input as ti


def start():
    view.showInfo("hello! welcome to our phonebook!")
    while True:
        
        op = view.getValue(f"input import or export mode and txt or csv format (IT / IC / ET / EC) {model.op_cod}")
        
        if ti.test_operations(op, model.operations.keys()):
            break
        else:
            view.showInfo("not correct input")

    model.operations[op]()