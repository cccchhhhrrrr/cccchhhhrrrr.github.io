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
      <td>Jappo</td>
      <td>350.0</td>
      <td>365</td>
      <td>3068</td>
      <td>8.41</td>
    </tr>
    <tr>
      <td>Kenk</td>
      <td>349.9</td>
      <td>344</td>
      <td>2946</td>
      <td>8.56</td>
    </tr>
    <tr>
      <td>Chrelle</td>
      <td>350.0</td>
      <td>354</td>
      <td>2939</td>
      <td>8.30</td>
    </tr>
    <tr>
      <td>Hustlersen</td>
      <td>327.8</td>
      <td>306</td>
      <td>2604</td>
      <td>8.51</td>
    </tr>
    <tr>
      <td>Visti</td>
      <td>350.0</td>
      <td>355</td>
      <td>2563</td>
      <td>7.22</td>
    </tr>
    <tr>
      <td>Tommy</td>
      <td>350.0</td>
      <td>338</td>
      <td>2512</td>
      <td>7.43</td>
    </tr>
    <tr>
      <td>Jarma</td>
      <td>350.0</td>
      <td>316</td>
      <td>2469</td>
      <td>7.81</td>
    </tr>
    <tr>
      <td>Matti</td>
      <td>349.1</td>
      <td>357</td>
      <td>2463</td>
      <td>6.90</td>
    </tr>
    <tr>
      <td>Okholm</td>
      <td>350.0</td>
      <td>361</td>
      <td>2460</td>
      <td>6.81</td>
    </tr>
    <tr>
      <td>Knak</td>
      <td>349.8</td>
      <td>340</td>
      <td>2449</td>
      <td>7.20</td>
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