from fasthtml.common import Style

global_style = Style(
  # align-items: center;
  """
  body {
    background-color: #000;
    color: #EEE;
    font-family: monospace;
    display: flex;
    justify-content: center;
    margin: 100px;
    font-size: 16px;
    line-height: 1.5;
  }
  div {
    width: 500px;
    padding: 20px;
    text-align: left;     
  }
  h2, h3 {
      color: #DDD;
  }
  a {
    color: #EEE;
  }
  .vertspace {
    margin: 14px 0;
  }
  """
)
