import model
import view
import test_input as ti


def start():
    view.showInfo("Привет! Это твоя телефонная книга!")
    while True:
        
        op = view.getValue(f"режим ввода импорта или экспорта выбери формат txt или csv (IT / IC / ET / EC) {model.op_cod}")
        
        if ti.test_operations(op, model.operations.keys()):
            break
        else:
            view.showInfo("not correct input")

    model.operations[op]()