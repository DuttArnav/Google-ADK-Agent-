from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import asyncio
from My_Agent import agent

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'Message is required'}), 400
        
        # Run the agent asynchronously
        async def get_response():
            response_parts = []
            async for chunk in agent.root_agent.run_async(user_message):
                response_parts.append(str(chunk))
            return ''.join(response_parts)
        
        # Run the async function
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(get_response())
        loop.close()
        
        return jsonify({'response': response})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)




