---
hide:
  - toc
---

<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title> C Y K E L V E N N E R </title>

    <style>

      body {
        font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
      }

      table {
        font-size: 11px;
        border-collapse: collapse;
        width: 90%;
      }
      
      td, th {
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
      }
      
      </style>
  </head>
  <body>
  <table border="1" class="dataframe" id="filterabletable">
  <thead>
    <tr style="text-align: right;">
      <th>ManagerName</th>
      <th>Pris</th>
      <th>Løbsdage</th>
      <th>Point</th>
      <th>Point per løbsdag</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Chrelle</td>
      <td>350.0</td>
      <td>668</td>
      <td>5788</td>
      <td>8.66</td>
    </tr>
    <tr>
      <td>Jappo</td>
      <td>350.0</td>
      <td>629</td>
      <td>5406</td>
      <td>8.59</td>
    </tr>
    <tr>
      <td>Kenk</td>
      <td>349.9</td>
      <td>601</td>
      <td>5164</td>
      <td>8.59</td>
    </tr>
    <tr>
      <td>Tommy</td>
      <td>350.0</td>
      <td>597</td>
      <td>4872</td>
      <td>8.16</td>
    </tr>
    <tr>
      <td>Okholm</td>
      <td>350.0</td>
      <td>660</td>
      <td>4782</td>
      <td>7.25</td>
    </tr>
    <tr>
      <td>Knak</td>
      <td>349.8</td>
      <td>619</td>
      <td>4779</td>
      <td>7.72</td>
    </tr>
    <tr>
      <td>Visti</td>
      <td>350.0</td>
      <td>625</td>
      <td>4736</td>
      <td>7.58</td>
    </tr>
    <tr>
      <td>Matti</td>
      <td>349.1</td>
      <td>628</td>
      <td>4546</td>
      <td>7.24</td>
    </tr>
    <tr>
      <td>Hustlersen</td>
      <td>327.8</td>
      <td>605</td>
      <td>4389</td>
      <td>7.25</td>
    </tr>
    <tr>
      <td>Jarma</td>
      <td>350.0</td>
      <td>583</td>
      <td>4358</td>
      <td>7.48</td>
    </tr>
  </tbody>
</table>
<script src="../js/tablefilter/tablefilter.js"></script>

  <script data-config>
    var tfConfig = {
      base_path: '../js/tablefilter/',
      alternate_rows: true,
      btn_reset: {
          text: 'Nulstil'
      },
      auto_filter: {
        delay: 1100 //milliseconds
      },
 
      loader: true,
      no_results_message: true,  

      // columns data types
      col_types: [
          'string',
          { type: 'formatted-number', decimal: '.', thousands: ',' },
          'number',
          'number',
          { type: 'formatted-number', decimal: '.', thousands: ',' },
      ],

      // Sort extension: in this example the column data types are provided by the
      // 'col_types' property. The sort extension also has a 'types' property
      // defining the columns data type for column sorting. If the 'types'
      // property is not defined, the sorting extension will fallback to
      // the 'col_types' definitions.
      extensions: [{ name: 'sort' }]
  };

  var tf = new TableFilter('filterabletable', tfConfig);
  tf.init();
</script>
    
  </body>
</html>