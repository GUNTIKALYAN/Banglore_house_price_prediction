function updateSqftValue() {
  const val = document.getElementById("uiSqft").value;
  document.getElementById("sqftValue").innerText = val;
}

function changeSqft(step) {
  const slider = document.getElementById("uiSqft");
  let newVal = parseInt(slider.value) + step;
  if (newVal >= parseInt(slider.min) && newVal <= parseInt(slider.max)) {
    slider.value = newVal;
    updateSqftValue();
  }
}


function getBathValue() {
  const uiBathrooms = document.getElementsByName("uiBathrooms");
  for (let i = 0; i < uiBathrooms.length; i++) {
    if (uiBathrooms[i].checked) {
      return parseInt(uiBathrooms[i].value);
    }
  }
  return -1;
}

function getBHKValue() {
  const uiBHK = document.getElementsByName("uiBHK");
  for (let i = 0; i < uiBHK.length; i++) {
    if (uiBHK[i].checked) {
      return parseInt(uiBHK[i].value);
    }
  }
  return -1;
}

function onClickedEstimatePrice() {
  const sqft = document.getElementById("uiSqft");
  const bhk = getBHKValue();
  const bathrooms = getBathValue();
  const location = document.getElementById("uiLocations");
  const estPrice = document.getElementById("uiEstimatedPrice");

  const sqftValue = parseFloat(sqft.value);

  if (isNaN(sqftValue) || sqftValue < 100 || bhk === -1 || bathrooms === -1 || !location.value) {
    estPrice.textContent = "⚠️ Please fill all fields correctly.";
    estPrice.style.color = "red";
    return;
  }

  const url = "http://127.0.0.1:5000/predict_home_price";

  $.post(url, {
    total_sqft: sqftValue,
    bhk: bhk,
    bath: bathrooms,
    location: location.value
  }, function (data, status) {
    if (data.estimated_price !== undefined) {
      estPrice.textContent = `${data.estimated_price} Lakh`;
      estPrice.style.color = "#10b981"; // green
    } else {
      estPrice.textContent = "❌ Something went wrong. Try again.";
      estPrice.style.color = "red";
    }
  }).fail(function () {
    estPrice.textContent = "🚫 Server error. Make sure Flask is running.";
    estPrice.style.color = "red";
  });
}

function onPageLoad() {
  const url = "http://127.0.0.1:5000/get_location_names";

  $.get(url, function (data) {
    if (data && data.locations) {
      const uiLocations = document.getElementById("uiLocations");
      $('#uiLocations').empty();
      data.locations.forEach(location => {
        const opt = new Option(location, location);
        $('#uiLocations').append(opt);
      });
    }
  }).fail(function () {
    console.error("Failed to fetch location data.");
  });

  const sqftInput = document.getElementById("uiSqft");
  const sqftLabel = document.getElementById("sqftValue");
  if (sqftInput && sqftLabel) {
    sqftInput.addEventListener("input", function () {
      sqftLabel.textContent = this.value;
    });
  }
}

window.onload = onPageLoad;
