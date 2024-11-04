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
  .full-container {
    width: 500px;
    padding: 20px;
    text-align: left;
  }
  .list-entries {
    width: 500px;
    padding: 20px;
    text-align: left;
  }
  h2, h3 {
      color: #DDD;
  }
  h4 {
    margin-top: 5px;
    margin-bottom: 30px;
    display: inline-block;
    font-size: 18px;
    text-decoration: none;
  }
  a {
    color: #CCC;
    text-decoration: none;
    border: 2px solid white;
    padding: 5px;
    border-radius: 10px;
  }
  .vertspace {
    margin: 14px 0;
  }
  """
)
