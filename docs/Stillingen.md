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
      <td>429</td>
      <td>4255</td>
      <td>9.92</td>
    </tr>
    <tr>
      <td>Jappo</td>
      <td>350.0</td>
      <td>437</td>
      <td>4192</td>
      <td>9.59</td>
    </tr>
    <tr>
      <td>Kenk</td>
      <td>349.9</td>
      <td>415</td>
      <td>3955</td>
      <td>9.53</td>
    </tr>
    <tr>
      <td>Tommy</td>
      <td>350.0</td>
      <td>401</td>
      <td>3626</td>
      <td>9.04</td>
    </tr>
    <tr>
      <td>Knak</td>
      <td>349.8</td>
      <td>409</td>
      <td>3567</td>
      <td>8.72</td>
    </tr>
    <tr>
      <td>Jarma</td>
      <td>350.0</td>
      <td>378</td>
      <td>3498</td>
      <td>9.25</td>
    </tr>
    <tr>
      <td>Visti</td>
      <td>350.0</td>
      <td>410</td>
      <td>3455</td>
      <td>8.43</td>
    </tr>
    <tr>
      <td>Matti</td>
      <td>349.1</td>
      <td>436</td>
      <td>3397</td>
      <td>7.79</td>
    </tr>
    <tr>
      <td>Okholm</td>
      <td>350.0</td>
      <td>428</td>
      <td>3396</td>
      <td>7.93</td>
    </tr>
    <tr>
      <td>Hustlersen</td>
      <td>327.8</td>
      <td>372</td>
      <td>3368</td>
      <td>9.05</td>
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