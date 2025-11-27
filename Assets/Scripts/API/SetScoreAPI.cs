using UnityEngine;
using UnityEngine.Networking;
using System.Collections;

public class ScoreAPI : MonoBehaviour
{
    public IEnumerator SendScore(int score)
    {
        string jsonBody = $"{{\"score\": {score}}}";
        byte[] bodyRaw = System.Text.Encoding.UTF8.GetBytes(jsonBody);

        using (UnityWebRequest request =
           new UnityWebRequest("http://localhost:5000/score", "POST"))
        {
            request.uploadHandler = new UploadHandlerRaw(bodyRaw);
            request.downloadHandler = new DownloadHandlerBuffer();
            request.SetRequestHeader("Content-Type", "application/json");

            yield return request.SendWebRequest();

            if (request.result == UnityWebRequest.Result.Success)
                Debug.Log("Score Uploaded: " + request.downloadHandler.text);
            else
                Debug.LogError("Upload Error: " + request.error);
        }
    }
}
