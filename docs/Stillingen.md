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
      <td>Hustlersen</td>
      <td>327.8</td>
      <td>111</td>
      <td>780</td>
      <td>7.03</td>
    </tr>
    <tr>
      <td>Chrelle</td>
      <td>350.0</td>
      <td>102</td>
      <td>761</td>
      <td>7.46</td>
    </tr>
    <tr>
      <td>Kenk</td>
      <td>349.9</td>
      <td>98</td>
      <td>694</td>
      <td>7.08</td>
    </tr>
    <tr>
      <td>Jappo</td>
      <td>350.0</td>
      <td>96</td>
      <td>590</td>
      <td>6.15</td>
    </tr>
    <tr>
      <td>Matti</td>
      <td>349.1</td>
      <td>98</td>
      <td>584</td>
      <td>5.96</td>
    </tr>
    <tr>
      <td>Tommy</td>
      <td>350.0</td>
      <td>103</td>
      <td>506</td>
      <td>4.91</td>
    </tr>
    <tr>
      <td>Visti</td>
      <td>350.0</td>
      <td>88</td>
      <td>501</td>
      <td>5.69</td>
    </tr>
    <tr>
      <td>Okholm</td>
      <td>350.0</td>
      <td>90</td>
      <td>484</td>
      <td>5.38</td>
    </tr>
    <tr>
      <td>Knak</td>
      <td>349.8</td>
      <td>86</td>
      <td>404</td>
      <td>4.70</td>
    </tr>
    <tr>
      <td>Jarma</td>
      <td>350.0</td>
      <td>67</td>
      <td>310</td>
      <td>4.63</td>
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