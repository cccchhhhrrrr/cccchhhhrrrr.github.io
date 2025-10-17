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
      <td>1251</td>
      <td>11207</td>
      <td>8.96</td>
    </tr>
    <tr>
      <td>Jappo</td>
      <td>350.0</td>
      <td>1208</td>
      <td>9805</td>
      <td>8.12</td>
    </tr>
    <tr>
      <td>Kenk</td>
      <td>349.9</td>
      <td>1166</td>
      <td>9538</td>
      <td>8.18</td>
    </tr>
    <tr>
      <td>Knak</td>
      <td>349.8</td>
      <td>1228</td>
      <td>9299</td>
      <td>7.57</td>
    </tr>
    <tr>
      <td>Visti</td>
      <td>350.0</td>
      <td>1248</td>
      <td>9193</td>
      <td>7.37</td>
    </tr>
    <tr>
      <td>Okholm</td>
      <td>350.0</td>
      <td>1223</td>
      <td>9097</td>
      <td>7.44</td>
    </tr>
    <tr>
      <td>Tommy</td>
      <td>350.0</td>
      <td>1147</td>
      <td>8748</td>
      <td>7.63</td>
    </tr>
    <tr>
      <td>Jarma</td>
      <td>350.0</td>
      <td>1250</td>
      <td>8631</td>
      <td>6.90</td>
    </tr>
    <tr>
      <td>Hustlersen</td>
      <td>327.8</td>
      <td>1153</td>
      <td>8488</td>
      <td>7.36</td>
    </tr>
    <tr>
      <td>Matti</td>
      <td>349.1</td>
      <td>1238</td>
      <td>8028</td>
      <td>6.48</td>
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