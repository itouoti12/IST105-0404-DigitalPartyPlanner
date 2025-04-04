<?php
$localIp=$_SERVER[ 'SERVER_ADDR' ];
$publicIpcmd = escapeshellcmd("ec2-metadata -v");
$publicIp = shell_exec($publicIpcmd);
?>
<html>
<h1>Welcome to the Digital Party Planner Application!</h1>
<h2>This application is hosted on my EC2 instance with Public IP:<?php echo $publicIp; ?></h2>
<h2>Select party items you need.</h2>
<form action="process.php" method="post">


<!-- 0: Cake (value = 20)
1: Balloons (value = 21)
2: Music System (value = 10)
3: Lights (value = 5)
4: Catering Service (value = 8)
5: DJ (value = 3)
6: Photo Booth (value = 15)
7: Tables (value = 7)
8: Chairs (value = 12)
9: Drinks (value = 6)
10: Party Hats (value = 9)
11: Streamers (value = 18)
12: Invitation Cards (value = 4)
13: Party Games (value = 2)
14: Cleaning Service (value = 11) -->


<input type="checkbox" id="cake" name="party_items[]" value="20">
<label for="cake">Cake</label><br>
<input type="checkbox" id="balloons" name="party_items[]" value="21">
<label for="balloons">Balloons</label><br>
<input type="checkbox" id="music-system" name="party_items[]" value="10">
<label for="music-system">Music System</label><br>
<input type="checkbox" id="lights" name="party_items[]" value="5">
<label for="lights">Lights</label><br>
<input type="checkbox" id="catering-service" name="party_items[]" value="8">
<label for="catering-service">Catering Service</label><br>
<input type="checkbox" id="dj" name="party_items[]" value="3">
<label for="dj">DJ</label><br>
<input type="checkbox" id="photo-booth" name="party_items[]" value="15">
<label for="photo-booth">Photo Booth</label><br>
<input type="checkbox" id="tables" name="party_items[]" value="7">
<label for="tables">Tables</label><br>
<input type="checkbox" id="chairs" name="party_items[]" value="12">
<label for="chairs">Chairs</label><br>
<input type="checkbox" id="drinks" name="party_items[]" value="6">
<label for="drinks">Drinks</label><br>
<input type="checkbox" id="party-hats" name="party_items[]" value="9">
<label for="party-hats">Party Hats</label><br>
<input type="checkbox" id="streamers" name="party_items[]" value="18">
<label for="streamers">Streamers</label><br>
<input type="checkbox" id="invitation" name="party_items[]" value="4">
<label for="invitation">Invitation</label><br>
<input type="checkbox" id="party-games" name="party_items[]" value="2">
<label for="party-games">Party Games</label><br>
<input type="checkbox" id="cleaning-service" name="party_items[]" value="11">
<label for="cleaning-service">Cleaning Service</label><br>

<input type="submit" value="Submit">
</form>
</html>