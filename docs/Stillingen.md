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
      <td>441</td>
      <td>4495</td>
      <td>10.19</td>
    </tr>
    <tr>
      <td>Jappo</td>
      <td>350.0</td>
      <td>446</td>
      <td>4347</td>
      <td>9.75</td>
    </tr>
    <tr>
      <td>Kenk</td>
      <td>349.9</td>
      <td>423</td>
      <td>4129</td>
      <td>9.76</td>
    </tr>
    <tr>
      <td>Tommy</td>
      <td>350.0</td>
      <td>410</td>
      <td>3793</td>
      <td>9.25</td>
    </tr>
    <tr>
      <td>Knak</td>
      <td>349.8</td>
      <td>416</td>
      <td>3701</td>
      <td>8.90</td>
    </tr>
    <tr>
      <td>Visti</td>
      <td>350.0</td>
      <td>419</td>
      <td>3650</td>
      <td>8.71</td>
    </tr>
    <tr>
      <td>Matti</td>
      <td>349.1</td>
      <td>445</td>
      <td>3616</td>
      <td>8.13</td>
    </tr>
    <tr>
      <td>Jarma</td>
      <td>350.0</td>
      <td>383</td>
      <td>3540</td>
      <td>9.24</td>
    </tr>
    <tr>
      <td>Okholm</td>
      <td>350.0</td>
      <td>437</td>
      <td>3521</td>
      <td>8.06</td>
    </tr>
    <tr>
      <td>Hustlersen</td>
      <td>327.8</td>
      <td>382</td>
      <td>3421</td>
      <td>8.96</td>
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