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
      <td>61</td>
      <td>510</td>
      <td>8.36</td>
    </tr>
    <tr>
      <td>Chrelle</td>
      <td>350.0</td>
      <td>46</td>
      <td>422</td>
      <td>9.17</td>
    </tr>
    <tr>
      <td>Kenk</td>
      <td>349.9</td>
      <td>45</td>
      <td>342</td>
      <td>7.60</td>
    </tr>
    <tr>
      <td>Jappo</td>
      <td>350.0</td>
      <td>38</td>
      <td>288</td>
      <td>7.58</td>
    </tr>
    <tr>
      <td>Tommy</td>
      <td>350.0</td>
      <td>60</td>
      <td>285</td>
      <td>4.75</td>
    </tr>
    <tr>
      <td>Okholm</td>
      <td>350.0</td>
      <td>39</td>
      <td>253</td>
      <td>6.49</td>
    </tr>
    <tr>
      <td>Knak</td>
      <td>349.8</td>
      <td>45</td>
      <td>242</td>
      <td>5.38</td>
    </tr>
    <tr>
      <td>Visti</td>
      <td>350.0</td>
      <td>26</td>
      <td>167</td>
      <td>6.42</td>
    </tr>
    <tr>
      <td>Jarma</td>
      <td>350.0</td>
      <td>24</td>
      <td>113</td>
      <td>4.71</td>
    </tr>
    <tr>
      <td>Matti</td>
      <td>349.1</td>
      <td>25</td>
      <td>111</td>
      <td>4.44</td>
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