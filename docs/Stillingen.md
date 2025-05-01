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
      <td>421</td>
      <td>4219</td>
      <td>10.02</td>
    </tr>
    <tr>
      <td>Jappo</td>
      <td>350.0</td>
      <td>431</td>
      <td>4147</td>
      <td>9.62</td>
    </tr>
    <tr>
      <td>Kenk</td>
      <td>349.9</td>
      <td>409</td>
      <td>3919</td>
      <td>9.58</td>
    </tr>
    <tr>
      <td>Tommy</td>
      <td>350.0</td>
      <td>393</td>
      <td>3581</td>
      <td>9.11</td>
    </tr>
    <tr>
      <td>Knak</td>
      <td>349.8</td>
      <td>405</td>
      <td>3522</td>
      <td>8.70</td>
    </tr>
    <tr>
      <td>Jarma</td>
      <td>350.0</td>
      <td>375</td>
      <td>3498</td>
      <td>9.33</td>
    </tr>
    <tr>
      <td>Visti</td>
      <td>350.0</td>
      <td>406</td>
      <td>3398</td>
      <td>8.37</td>
    </tr>
    <tr>
      <td>Hustlersen</td>
      <td>327.8</td>
      <td>365</td>
      <td>3364</td>
      <td>9.22</td>
    </tr>
    <tr>
      <td>Okholm</td>
      <td>350.0</td>
      <td>422</td>
      <td>3347</td>
      <td>7.93</td>
    </tr>
    <tr>
      <td>Matti</td>
      <td>349.1</td>
      <td>426</td>
      <td>3340</td>
      <td>7.84</td>
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