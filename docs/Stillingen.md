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
      <td>170</td>
      <td>1334</td>
      <td>7.85</td>
    </tr>
    <tr>
      <td>Hustlersen</td>
      <td>327.8</td>
      <td>154</td>
      <td>1141</td>
      <td>7.41</td>
    </tr>
    <tr>
      <td>Kenk</td>
      <td>349.9</td>
      <td>151</td>
      <td>1131</td>
      <td>7.49</td>
    </tr>
    <tr>
      <td>Jappo</td>
      <td>350.0</td>
      <td>158</td>
      <td>1118</td>
      <td>7.08</td>
    </tr>
    <tr>
      <td>Matti</td>
      <td>349.1</td>
      <td>163</td>
      <td>1034</td>
      <td>6.34</td>
    </tr>
    <tr>
      <td>Okholm</td>
      <td>350.0</td>
      <td>159</td>
      <td>1004</td>
      <td>6.31</td>
    </tr>
    <tr>
      <td>Tommy</td>
      <td>350.0</td>
      <td>140</td>
      <td>919</td>
      <td>6.56</td>
    </tr>
    <tr>
      <td>Knak</td>
      <td>349.8</td>
      <td>134</td>
      <td>890</td>
      <td>6.64</td>
    </tr>
    <tr>
      <td>Jarma</td>
      <td>350.0</td>
      <td>125</td>
      <td>867</td>
      <td>6.94</td>
    </tr>
    <tr>
      <td>Visti</td>
      <td>350.0</td>
      <td>138</td>
      <td>856</td>
      <td>6.20</td>
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