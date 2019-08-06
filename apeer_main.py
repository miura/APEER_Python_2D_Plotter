from apeer_dev_kit import adk
import hello_world

if __name__ == "__main__":
    inputs = adk.get_inputs()

    outputs = hello_world.execute(inputs['Input'])

    adk.set_file_output('Output', outputs['Output'])
    adk.finalize()