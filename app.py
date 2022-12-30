import os

import click
import dotenv
import openai

dotenv.load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

@click.command()
@click.pass_context
@click.option('--input', type=click.File('rb'))
@click.option('--temperature', default=1, type=float)
def cli(ctx, input, temperature):
    parameters = {
        "model": "code-davinci-edit-001",
        "input": "",
        "temperature": temperature,
    }

    code = ""

    if input:
        while True:
            chunk = input.read(1024).decode('utf8')
            if not chunk:
                break
            code += chunk

        if code:
            parameters['input'] = code.strip()

    while True:
        click.echo(parameters['input'])

        instruction = click.prompt('', prompt_suffix='>>> ')

        # :q quits the application
        if instruction == ':q':
            ctx.exit(-1)

        # :u undoes the last change
        if instruction == ':u':
            parameters['input'] = previous_input
            continue

        # :w followed by a filename writes the current input to a file
        if instruction.startswith(':w'):
            filename = instruction[2:].strip()
            with open(filename, 'wb') as output:
                output.write(parameters['input'].encode('utf8'))
            continue

        parameters['instruction'] = instruction

        response = openai.Edit.create(**parameters)

        previous_input = parameters['input']
        parameters['input'] = response['choices'][0]['text']
