def llm_stream_response(stream):
    for chunk in stream:
        yield chunk.content
